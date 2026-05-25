---
type: deity
source-type: "Remaster"
domains: "Darkness, Indulgence, Water, Wealth"
favored-weapon: "Halberd"
divine-font: "Harm, Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Animal Allies]], Rank 4: [[Hydraulic Torrent]], Rank 8: [[Desiccate]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Tyrants, greedy landlords, and corrupt governments suck their constituents dry in pursuit of their own fortunes, and Tresmalvos welcomes them all to the harbinger's water-logged, rotting bosom. The Cistern Queen is the unquestioned ruler of her domain, a sprawling labyrinth of dark sewer tunnels decorated with the befouled trappings of the wealthy. Though the indulgent wealthy do her work without knowing it, Tresmalvos is often petitioned by those of lowlier stations (such as rat catchers) in the hopes of inverting the current power structure. Occasionally, the Cistern Queen will grant such a request (usually via her swarms of filthy rats), elevating a worshipper to a higher status, only to entice them into acting the same way as their former oppressors.

**Title** The Cistern Queen

**Areas of Concern** All-consuming greed, befouled sewers, cesspools, rat catchers

**Edicts** Chase material wealth, oppress the less fortunate, think only of the current moment

**Anathema** Give a gift without expectation of reciprocation, participate in maintaining urban infrastructure

**Religious Symbol** rat skull with crown

**Sacred Animal** rat

**Sacred Colors** black, red

**Source:** `= this.source` (`= this.source-type`)
