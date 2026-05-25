---
type: deity
source-type: "Remaster"
domains: "Death, Indulgence, Might, Pain"
favored-weapon: "Greataxe"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Grim Tendrils]], Rank 3: [[Moth'S Supper]], Rank 9: [[Implosion]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Nulgreth is one of the oldest orc deities, and is thought to be the origin of the ferocity that allows orcs to lash out in battle even when slain. If nothing else, he's certainly a prime example of that ferocity due to his constant rage and endless bloodlust. One need not worry about him scheming or plotting, just the sharp edge of his axe.

**Title** The Blood God

**Areas of Concern** Blood, rage, strength

**Edicts** Bathe in the blood of your fallen enemies, face your enemies head-on, never turn down a fight you can win

**Anathema** Grant or accept mercy, take prisoners, perform underhanded tricks

**Religious Symbol** bloody double-axe

**Sacred Animal** wolverine

**Sacred Colors** green, red

**Source:** `= this.source` (`= this.source-type`)
