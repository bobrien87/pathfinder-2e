---
type: deity
source-type: "Remaster"
domains: "Air, Confidence, Passion, Sun"
favored-weapon: "Main-gauche"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Charm]], Rank 3: [[Wall Of Radiance]], Rank 5: [[Cloak Of Colors]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Sturovenen was born to the second generation of spirit guides, the mighty son of Dragon and Eagle. Noble, kind, and a leader by example, Sturovenen's worship spread quickly and he ascended to full godhood in astonishingly short order. Sturovenen had two great loves: the mortal man Chakli, who became Sturovenen's first god caller, and the spirit guide Canary

**Title** The Dragoneagle

**Areas of Concern** Leadership, righteous battle, the sun

**Edicts** Act with conviction and confidence, be a passionate and responsible leader to your people or companions

**Anathema** Command a subordinate to perform a task you're not willing to perform yourself

**Religious Symbol** gold-feathered wing

**Sacred Animal** snake

**Sacred Colors** green, purple, yellow

**Source:** `= this.source` (`= this.source-type`)
