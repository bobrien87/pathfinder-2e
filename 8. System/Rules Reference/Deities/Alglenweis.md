---
type: deity
source-type: "Remaster"
domains: "Cold, Creation, Might, Soul"
favored-weapon: "War-flail"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Agitate]], Rank 4: [[Creation]], Rank 5: [[Howling Blizzard]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Called the Princess of the Rime by some, Alglenweis is the most popular Sarkorian deity in the Realm of the Mammoth Lords; though, since the opening of the Worldwound, her worship in Sarkoris has dwindled. Her ties to demonic entities like her father have placed her in a position of mistrust among Sarkorians who fear the return of a malevolent entity like Deskari.

**Title** Princess of the Rime

**Areas of Concern** Crafting, resolve, winter

**Edicts** Protect the monuments of your people, stir others into action, strive to perfect an art or craft

**Anathema** Destroy an artistic creation without providing something in its place, refuse to act if called upon

**Religious Symbol** owl talon clutching a frozen skein of yarn

**Sacred Animal** owl

**Sacred Colors** light blue, light green, white

**Source:** `= this.source` (`= this.source-type`)
