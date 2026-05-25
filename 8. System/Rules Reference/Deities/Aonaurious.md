---
type: deity
source-type: "Remaster"
domains: "Ambition, Death, Might, Travel"
favored-weapon: "Scythe"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Grim Tendrils]], Rank 3: [[Haste]], Rank 5: [[Moon Frenzy]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Aonaurious appears as a sleek insectile creature with an obsidian carapace and razor-sharp claws that drip with blood. A quartet of unblinking eyes are spaced evenly around his head so that he can see in all directions and dozens of legs provide him the speed to pursue any prey. Called the Enigma Clot, he is the most violently aggressive qlippoth lord, always ready to wade into battles against demons and mortals alike. He grants no quarter, expects none in return and will mercilessly chase any who flee from a fight until he can tear them to pieces.

**Title** The Enigma Clot

**Areas of Concern** Bloodshed, tireless pursuit, wrathful combat

**Edicts** Spill blood, use any method necessary to kill, vent your wrath on any and all

**Anathema** Allow a quarry to escape, stanch a bleeding wound

**Religious Symbol** claw-shaped rune drawn in blood

**Sacred Animal** none

**Sacred Colors** black

**Source:** `= this.source` (`= this.source-type`)
