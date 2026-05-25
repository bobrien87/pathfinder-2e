---
type: deity
source-type: "Remaster"
domains: "Ambition, Might, Truth, Zeal"
favored-weapon: "Javelin"
divine-font: "Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Ant Haul]], Rank 2: [[Enlarge]], Rank 3: [[Haste]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Once a mortal farm boy from Taldor who had superhuman strength from youth, Kurgess's selfless sacrifice on the field of competition heralded his rise to godhood. Known as the Strong Man, Kurgess stands as both champion and shining example to those who seek athletic achievement and to give their all in competition, regardless of whether they are victorious or not.

**Title** The Strong Man

**Areas of Concern** healthy competition, sport, physical development

**Edicts** compete to your full potential, claim victory or accept defeat with grace, seek always to better yourself, encourage others to strive toward their own potential for greatness

**Anathema** cheat at honorable contests, dishonor those who have lost or failed (including defeated or slain enemies), engage in reckless or needless destruction or bloodshed

**Religious Symbol** flexing arm with chain

**Sacred Animal** horse

**Sacred Color** gold, white

**Source:** `= this.source` (`= this.source-type`)
