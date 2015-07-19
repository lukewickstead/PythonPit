function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        }
    }
});

$(document).ready(function () {
    $("#getquote").click(function () {
        getQuote();
    });

    $("#getAuthorQuotes").click(function () {
        getAuthorQuotes();
    });

    $("#newquote").click(function () {
        createNewQuote();
    });
});

function getQuote() {
    $.getJSON("/ajax/random", function (data) {
        console.log("getQuote.response:");
        console.log(data);
        $.each(data, function (author, quote) {
            $('#quote').text(quote);
            $('#author').text(author);
        });
    });
}

function getAuthorQuotes() {
    $.getJSON("/ajax/author/", {author: $('#authors').val()}, function (data) {
            console.log("getAuthorQuotes.response:");
            console.log(data);

            var $quotesbyauthor = $('#quotesbyauthor');
            $quotesbyauthor.text("");

            var items = [];

            $.each(data, function (key, value) {
                items.push("<ul>" + value.fields["quote"] + ". " + value.fields["author"] + "</ul>");
            });

            $("<ul/>", {
                "class": "quotes",
                html: items.join("")
            }).appendTo($quotesbyauthor);
        }
    );
}

function createNewQuote() {
    $.ajax({
        type: "POST",
        url: "/ajax/new/",
        data: {
            'quote': $('#txtquote').val(),
            'author': $('#txtauthor').val()
        },
        success: function (data) {
            console.log("createNewQuote.response:");
            console.log(data);

            alert(data.message);

            if (data.created) {
                alert("There are now " + data.count + " quotes");
            }
        }
    });
}