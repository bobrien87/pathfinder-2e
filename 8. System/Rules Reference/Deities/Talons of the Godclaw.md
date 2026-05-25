---
type: deity
source-type: "Remaster"
domains: "Duty, Might, Perfection, Protection"
favored-weapon: "Morningstar"
divine-font: "Harm, Heal"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Sure Strike]], Rank 4: [[Mountain Resilience]], Rank 6: [[Flame Vortex]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

There are often many differences between diving beings in a pantheon, but sometimes universal concepts can still bind them together. The Hellknight Order of the Godclaw extols the virtues of five gods—Abadar, Asmodeus Iomedae, Irori, and Torag—as seen through a particular lens of order and discipline. Though many priests of each individual faith called such views inconceivable or even heretical, the Godclaw's faithful nevertheless receive divine power from their shared patrons. Due to a simultaneous rise in enlistment by those of orc ancestry in the ranks and endorsement by those faithful to Torag, the god Uirch has replaced the dwarven deity in this pantheon's ranks.

**Pantheon Members** Abadar, Asmodeus, Iomedae, Irori, Uirch

**Areas of Concern** balance, devotion, discipline, order

**Edicts** be an exemplar of divine order and balance, demonstrate the resilience of your faith by shielding others from chaos, instruct others who show promise in the ways of your order

**Anathema** profess to understand law or order better than the pantheon, take no action when the presence of chaos has been revealed

**Religious Symbol** five-pointed iron star

**Source:** `= this.source` (`= this.source-type`)
