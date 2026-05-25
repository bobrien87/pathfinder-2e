---
type: deity
source-type: "Remaster"
domains: "Darkness, Knowledge, Void, Time"
favored-weapon: "Sap"
divine-font: "Harm"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Penumbral Shroud]], Rank 3: [[Curse Of Lost Time]], Rank 5: [[Illusory Scene]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The One Out of Place is an apt title for Shawnari, often forgotten even by the other sahkil tormentors. Little is known about Shawnari's past, though it has been suggested that she abused her time as a psychopomp by trapping souls in secret places where she could watch them wither in solitude. Her interest in isolation continues in her divine form, reigning quietly over loneliness and lost time.

**Title** The One Out of Place

**Areas of Concern** Isolation, loneliness, lost time

**Edicts** Fiercely protect your privacy, rely only on yourself, waste time in frivolous pursuits

**Anathema** Keep strict track of your time, reach out to others when you feel alone

**Religious Symbol** shattered clock face

**Sacred Animal** cicada

**Sacred Colors** gray, green

**Source:** `= this.source` (`= this.source-type`)
