---
type: deity
source-type: "Remaster"
domains: "Ambition, Darkness, Nightmares, Trickery"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 3: [[Mind Reading]], Rank 5: [[Umbral Journey]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

This strange trio of feline eyes is the Forsaken patron of inferiority, cats, and strangers.

**Title** The Deep Gazer

**Areas of Concern** Cats, inferiority, strangers

**Edicts** Follow and observe others, remind others of their place

**Anathema** Act out against your superiors, become too familiar with someone, harm a cat

**Religious Symbol** Three feline eyes

**Sacred Animal** cat

**Sacred Colors** black, yellow

An owb prophet can transfer the power they gain from a Forsaken patron to those who worship them, effectively serving as a deity. Each owb prophet decides their own follower alignments, edicts, and anathema.

**Source:** `= this.source` (`= this.source-type`)
