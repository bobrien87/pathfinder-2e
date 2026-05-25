---
type: deity
source-type: "Remaster"
domains: "Creation, Freedom, Might, Wealth"
favored-weapon: "Longsword"
divine-font: "Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Ghostly Weapon]], Rank 5: [[Cloak Of Colors]]"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Femininity, martial training, and rings are the purview of the Warrior's Ring. In the eyes of Falayna, there is as much grace and beauty in the martial arts as exists in any culture's definition of femininity. The strength of womanhood is a hallmark of femininity, and strength in arms reflects this, with the flourish and personality of a fighting style a vibrant means for selfexpression. Followers of Falayna learn to fight so they can both express their body and defend themselves if necessary, and strive to feel beautiful doing so, both in form and in dress. Falayna also enjoys rings, and as such she is associated with events in which rings are given or exchanged, such as weddings.

**Title** Warrior's Ring

**Areas of Concern** Femininity, martial training, rings

**Edicts** Wear and make beautiful things, train for combat, recover and return lost mementos

**Anathema** Disrupt or destroy romantic unions, enforce a dress code, cower from fights

**Religious Symbol** sword held aloft

**Sacred Animal** cat

**Sacred Colors** silver, white

**Source:** `= this.source` (`= this.source-type`)
