---
type: deity
source-type: "Remaster"
domains: "Indulgence, Magic, Might, Undeath"
favored-weapon: "Scythe"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Goblin Pox]], Rank 2: [[False Vitality]], Rank 7: [[Mask Of Terror]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

May you dine forever. All things decay and are ultimately consumed, but for followers of Urgathoa there's divinity in the consumption and deterioration. Once a mortal, Urgathoa embraced life and all its pleasures. She never denied herself, and questioned the tenets of deities preaching that a person should restrain themselves while on the mortal plane, holding fast to a promise of eternal pleasures after death. Instead, she believed that Golarion housed a vast buffet of delights made for the living to feast upon. Urgathoa so loved satiating her life's appetites that in death, she spat in the face of Pharasma's judgment, murdered the psychopomp assigned to aid her transition to the afterlife, and tore herself from the Boneyard with a feat of will that not only returned her to the mortal Universe but also transformed her into the first undead creature and a god.

**Title** The Pallid Princess

**Areas of Concern** disease, gluttony, undeath

**Edicts** become undead upon death, create or protect the undead, sate your appetites

**Anathema** deny your appetites, destroy undead of no harm to you, sacrifice your life

**Religious Symbol** skull-decorated fly

**Sacred Animal** fly

**Sacred Colors** red, green

**Source:** `= this.source` (`= this.source-type`)
