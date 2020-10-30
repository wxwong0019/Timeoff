db.movie.find( {
    $and : [
        { $or : [ { genre:"Comedy" }, { genre:"Drama" },{ genre:"Horror" },{ genre:"Thriller" } ] },
        { genre: {$ne : "Foreign"} },
        { leadActors: {$ne : "Jodie Foster"}},
        { lengthInMin: {$lt : 120}}
} )