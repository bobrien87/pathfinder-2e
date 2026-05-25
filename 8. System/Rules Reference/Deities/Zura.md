---
type: deity
source-type: "Remaster"
domains: "Indulgence, Nightmares, Undeath, Delirium"
favored-weapon: "Rapier"
divine-font: "Harm"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Charm]], Rank 4: [[Vapor Form]], Rank 7: [[Mask Of Terror]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Zura, the Vampire Queen, is the demon lord of blood, cannibalism, and vampires. According to legend, she is the reincarnated form of an Azlanti queen who indulged in blood rites and acts of cannibalism in a quest for eternal life. After death, she was reborn as a unique vampiric succubus who quickly ascended to the status of demon lord. Though many of her cults died out with the Azlanti empire, Zura is still worshipped by vampires and those aspiring to become vampires, particularly within Cheliax and Ustalav, as well as some civilizations of the Darklands.

**Title** The Vampire Queen

**Areas of Concern** Blood, cannibalism, vampires

**Edicts** Drink blood, seek vampirism, cause bleed damage

**Anathema** Expose vampires, heal a bloody wound without drinking blood from it first

**Religious Symbol** crimson fanged skull rune

**Sacred Animal** vampire bat

**Sacred Colors** red

**Source:** `= this.source` (`= this.source-type`)
