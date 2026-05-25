---
type: deity
source-type: "Remaster"
domains: "Creation, Earth, Knowledge, Magic"
favored-weapon: "Dagger"
divine-font: "Heal"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Shattering Gem]], Rank 2: [[Shape Wood]], Rank 3: [[One With Stone]], Rank 4: [[Shape Stone]], Rank 5: [[Nature'S Pathway]], Rank 6: [[Tangling Creepers]], Rank 7: [[Unfettered Pack]], Rank 8: [[Burning Blossoms]], Rank 9: [[Nature'S Enmity]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Yuelral is the elven goddess of magic. She is a patron of both divine and arcane magic, but prefers magic that deals with the natural world rather than magic that deals with metal and other artificial things. She is frequently worshiped by jewelers because of her affinity with crystals. These jewelers never cut their crystals, instead embracing their natural beauty. Yuelral is quick to embrace half elves, seeing past their mixed heritage to what lies within.

**Title** The Wise

**Areas of Concern** Crystal, jewelers, magic

**Edicts** Practice herbalism, use and enchant gems, encourage and teach magicians and jewelers, preserve elven magic and knowledge

**Anathema** Cut a gem for aesthetic purposes, defile nature, allow the irresponsible use of magic

**Religious Symbol** three overlapping crystals

**Sacred Animal** panther

**Sacred Colors** blue, green, red

**Source:** `= this.source` (`= this.source-type`)
