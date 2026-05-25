---
type: deity
source-type: "Remaster"
domains: "Cities, Family, Repose, Protection"
favored-weapon: "Staff"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Endure]], Rank 4: [[Fire Shield]], Rank 9: [[Resplendent Mansion]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Some myths say that long before her marriage, Folgrit was the Goddess of Mourners, one who watched over and protected those left behind in bereavement after massive wars and calamities. She witnessed many dwarves, especially orphans, left adrift to fend for themselves against the world and the dwarven community at large. Determined to save these individuals from the fate of an outcast, she approached the then-bachelor Torag with a proposal: in exchange for her hand in marriage, he would share his powers of family and protection with her. The union was a celebrated affair for the pantheon. In addition to sharing the agreed-upon powers, Torag also gifted Folgrit oversight of settlements and cities, so that she could ensure those under her care shall always have shelter.

As the Watchful Mother, Folgrit's teachings cover many topics. The most common are practical lessons in homemaking, covering various essential life skills from cleaning, cooking, to maintenance. It is not uncommon, therefore, for many of her temples to house libraries or workshops full of recipes, manuals, tools, and cookware. For a non-worshipper, it can be difficult to determine where Folgrit's areas of concern end and Torag's begin, as they both seem to cover an aspect of crafting. Priests of either deity explain that Torag is involved in creation of items from its raw state, and repair of items that have been broken, particularly military or magical gear. Folgrit, meanwhile, covers maintenance and small fixes, and is usually concerned only with mundane items.

**Title** The Watchful Mother

**Areas of Concern** Children, hearths, mothers

**Edicts** Maintain the sanctity of a home, remain patient with others, take in those without families

**Anathema** Abandon your family, fail to defend your neighbors

**Religious Symbol** rune-carved hearth

**Sacred Animal** young animals

**Sacred Colors** gray, orange

**Source:** `= this.source` (`= this.source-type`)
