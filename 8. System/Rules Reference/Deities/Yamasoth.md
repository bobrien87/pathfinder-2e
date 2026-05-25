---
type: deity
source-type: "Remaster"
domains: "Abomination, Change, Earth, Pain"
favored-weapon: "Halberd"
divine-font: "Harm, Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Draw Ire]], Rank 4: [[Bestial Curse]], Rank 7: [[Mask Of Terror]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Yamasoth appears as a nightmarish octopus with a multitude of tentacles, each ending in a method of inflicting pain. His body is a single massive mouth filled with sharp teeth and stinging tongues. Eyes dot his form, and one huge red eye sits within his throat. Like all qlippoth lords, Yamasoth seeks to eradicate demons by eliminating sin in mortals, but his methods involve corrupting powerful leaders until they doom their kingdoms and performing terrible fleshwarping experiments on hapless victims to release monsters upon civilization. Yamasoth has a grudging respect tempered with disdain for Lamashtu for her hand in creating monsters but hates almost all other deities.

**Title** The Polymorph Plague

**Areas of Concern** Adaptation, cursed kingdoms, vile experiments

**Edicts** Embrace your worst aspects, perform dangerous experiments on yourself and others, whisper foul secrets in the ears of leaders

**Anathema** Avoid new experiences, try to steer a community away from a deadly fate

**Religious Symbol** circular rune with six spiraling arms around three eyes

**Sacred Animal** none

**Sacred Colors** red

**Source:** `= this.source` (`= this.source-type`)
