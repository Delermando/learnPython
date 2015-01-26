USE personare;
CREATE ALGORITHM=UNDEFINED VIEW `magazine_channels` AS select `mh`.`id` AS `id`,`mh`.`title` AS `title`,`mh`.`permalink` AS `permalink`,`mh`.`status` AS `status`,`mh`.`is_channel` AS `is_channel`,`mcd`.`idHome` AS `idHome`,`mcd`.`idEditorial` AS `idEditorial`,`mcd`.`idHeaderImage` AS `idHeaderImage`,`mcd`.`colour` AS `colour`,`mcd`.`second_colour` AS `second_colour`,`mcd`.`creationDate` AS `creationDate`,`mcd`.`publicationDate` AS `publicationDate`,`mcd`.`deactivationDate` AS `deactivationDate`,`mcd`.`displayOrder` AS `displayOrder`,`mcd`.`hasSeal` AS `hasSeal`,`mcd`.`parentidHome` AS `parentidHome`,`mcd`.`package` AS `package`,`mcd`.`link_intro` AS `link_intro`,`mcd`.`limit_module_more_articles` AS `limit_module_more_articles`,`mcd`.`enable_background_in_articles` AS `enable_background_in_articles` from (`magazine_channelsdata` `mcd` join `magazine_homes` `mh` on((`mh`.`id` = `mcd`.`idHome`)));
