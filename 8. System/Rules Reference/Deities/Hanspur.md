---
type: deity
source-type: "Remaster"
domains: "Death, Travel, Water, Wealth"
favored-weapon: "Trident"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Hydraulic Push]], Rank 3: [[Aqueous Orb]], Rank 5: [[Control Water]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

People often jump to the conclusion that Hanspur is a small god that cares only about the Sellen River, its tributaries in the River Kingdoms, and those who ply those waterways. But he is much more than that. This demigod believes that all people should be able to flow like rivers and not be dammed by laws or other imposed restrictions. Freedom is of paramount import to Hanspur, who exhorts his followers to let no one stand in the way of achieving their goals. This outlook makes the Water Rat a popular deity among smugglers, especially those who use rivers. Even Hanspur has transported illicit weapons and other goods to planar communities on the banks of the River Styx to help stem the advancement of daemons.

**Title** The Water Rat

**Areas of Concern** river travel, rivers, and smuggling

**Edicts** guard river travelers from unnatural hazards, learn how to live off the river, save others from drowning

**Anathema** aid daemons or the Riders of the Apocalypse, impose needless laws or restrictions on others

**Religious Symbol** rat walking on water

**Sacred Animal** rat

**Sacred Colors** blue, gold

**Source:** `= this.source` (`= this.source-type`)
