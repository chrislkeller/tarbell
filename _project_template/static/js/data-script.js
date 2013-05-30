var jqueryNoConflict = jQuery;
var fn = fn || {};

// begin main function
jqueryNoConflict(document).ready(function() {
    fn.retrieveDataFromFile();
});

// begin data configuration object
var fn = {

    // pull the data from the flat file
    retrieveDataFromFile: function(){
        jqueryNoConflict.getJSON(dataSource, fn.processDataFromFile);
    },

    processDataFromFile: function(data){
        console.log(data);
    }
};
// end data configuration object