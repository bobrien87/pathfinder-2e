---
type: deity
source-type: "Remaster"
domains: "Air, Creation, Protection, Toil"
favored-weapon: "Staff"
divine-font: "Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Phantasmal Minion]], Rank 3: [[Cozy Cabin]], Rank 6: [[Vibrant Pattern]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

There once was a weaver named Yelayne who was known far and wide for making the finest cloth and most beautiful garments, and one day the Wind fell in love with her. The Wind followed Yelayne everywhere, tugging on her hair and rumpling the beautiful clothing that she worked so hard to craft. She ignored him, because she was wise and knew the Wind could be fickle and cruel. When he persisted in pursuing her against her wishes, she brought out her most tightly-woven bag and whistled for the Wind's attention. When he came rushing, she trapped him in the bag. Ever afterward, she only let the Wind out if he promised to obey her. Yelayne had the Wind carry her all over the world, teaching the art of weaving to any who would work at it and learning how to make the most fantastical clothes. When she tired of that, she had the Wind carry her to Heaven, where she wove starlight into constellations, sunshine into rainbows, and moonbeams into enchantments. She still watches to make sure that none are left exposed for the old Wind to bother, and that all are able to pursue their creative endeavors, express themselves, and dress how they like.

**Title** The Wind Weaver

**Areas of Concern** Clothing, craftspeople, security, self-expression

**Edicts** Develop a signature style, express yourself through craft, provide necessities and protection for those in need

**Anathema** Steal another artisan's design, participate in an arranged marriage

**Religious Symbol** shining spool of thread

**Sacred Animal** weaver bird

**Sacred Colors** blue, silver

**Source:** `= this.source` (`= this.source-type`)
