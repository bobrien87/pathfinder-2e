---
type: deity
source-type: "Remaster"
domains: "Duty, Family, Moon, Protection"
favored-weapon: "Spear"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Protector Tree]], Rank 4: [[Containment]], Rank 6: [[Wall Of Force]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Acavna, the Shield, was one of humanity's fiercest protectors. Legends of her tactics and exploits spanned the entirety of the Azlanti Empire. Her most famous act of heroism led to her death during the events of Earthfall. Determined to protect her people, Acavna refused to stand down despite her partner Amaznen's pleas. She used her magic to move Golarion's moon in the way of the incoming meteor, absorbing most of the destructive blast. Her body fell from the sky and plunged into the planet's core. The Mordant Spire grew from her remains, and the elves who reside there claim to hear Acavna whispering to them.

**Title** The Shield

**Areas of Concern** Companionship, defensive tactics, the moon

**Edicts** Protect the weak and innocent, use defense as your first resource, make choices for the good of all and not the good of one

**Anathema** Attack without cause, ignore the pleas of the weak and innocent, act solely for your own self interest

**Religious Symbol** crossed spears over a full moon

**Sacred Animal** rabbit

**Sacred Colors** periwinkle

**Source:** `= this.source` (`= this.source-type`)
