{
    // The tab key will cycle through the settings when first created
    // Visit http://wbond.net/sublime_packages/sftp/settings for help
    
    // sftp, ftp or ftps
    "type": "sftp",

    "sync_down_on_open": true,
    "sync_same_age": true,
    
    "host": "121.42.176.120",
    "user": "joklin",
    "password": "",
    "port": "62919",
    
    "remote_path": "/home/joklin",
    //"file_permissions": "664",
    //"dir_permissions": "775",
    
    //"extra_list_connections": 0,

    "connect_timeout": 30,
    //"keepalive": 120,
    //"ftp_passive_mode": true,
    //"ftp_obey_passive_host": false,
    //"ssh_key_file": "~/.ssh/id_rsa",
    //"sftp_flags": ["-F", "/path/to/ssh_config"],
    
    //"preserve_modification_times": false,
    //"remote_time_offset_in_hours": 0,
    //"remote_encoding": "utf-8",
    //"remote_locale": "C",
    //"allow_config_upload": false,
}
$(function(){
/*widgest 中卷起的js*/
    $('.panel-close').click(function(){
        $(this{
            // The tab key will cycle through the settings when first created
            // Visit http://wbond.net/sublime_packages/sftp/settings for help
            
            // sftp, ftp or ftps
            "type": "sftp",
        
            "sync_down_on_open": true,
            "sync_same_age": true,
            
            "host": "example.com",
            "user": "username",
            //"password": "password",
            //"port": "22",
            
            "remote_path": "/example/path/",
            //"file_permissions": "664",
            //"dir_permissions": "775",
            
            //"extra_list_connections": 0,
        
            "connect_timeout": 30,
            //"keepalive": 120,
            //"ftp_passive_mode": true,
            //"ftp_obey_passive_host": false,
            //"ssh_key_file": "~/.ssh/id_rsa",
            //"sftp_flags": ["-F", "/path/to/ssh_config"],
            
            //"preserve_modification_times": false,
            //"remote_time_offset_in_hours": 0,
            //"remote_encoding": "utf-8",
            //"remote_locale": "C",
            //"allow_config_upload": false,
        }
        ).parent().parent().parent().hide(300);
    });

    $('.collapse').on('hide.bs.collapse',function(){
        $(this).prev().find(".panel-collapse").removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
    });

    $('.collapse').on('show.bs.collapse',function(){
        $(this).prev().find(".panel-collapse").removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
    });


});

/*提示的js*/
$(function () { $("[data-toggle='tooltip']").tooltip(); });
$('#nav-login').tooltip('hide');
