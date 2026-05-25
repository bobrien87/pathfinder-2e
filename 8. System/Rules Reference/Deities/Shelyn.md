---
type: deity
source-type: "Remaster"
domains: "Creation, Family, Passion, Protection"
favored-weapon: "Glaive"
divine-font: "Heal"
divine-skill: "Crafting, Performance"
divine-spells: "Rank 1: [[Dizzying Colors]], Rank 3: [[Enthrall]], Rank 4: [[Creation]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

To know Shelyn is to love her, for Shelyn embodies love, as well as beauty, art, and music. She seeks to spread these pursuits across Golarion, teaching that they are the best way to find peace and happiness. Her passion is such that even the most basic attempts at art delight her—the greatest marble sculptures of Taldor or kholo chants from the Mwangi Expanse are as beloved to her as the meanest sketches of a young orphan in Isger or the crude sand art of a Thuvian child. Beauty, for Shelyn, is a quality of being, not a specific set of characteristics, and she encourages people to find and accept many definitions of it.

**Title** The Eternal Rose

**Areas of Concern** art, beauty, love, music

**Edicts** be peaceful, choose and perfect an art, lead by example, see the beauty in all things

**Anathema** destroy art or allow it to be destroyed, unless saving a life or pursuing greater art; refuse to accept surrender

**Religious Symbol** multicolored songbird

**Sacred Animal** songbird

**Sacred Colors** all

**Source:** `= this.source` (`= this.source-type`)
