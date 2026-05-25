---
type: deity
source-type: "Remaster"
domains: "Might, Pain, Swarm, Zeal"
favored-weapon: "Kukri"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Sure Strike]], Rank 2: [[Animal Form]], Rank 5: [[Moon Frenzy]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Carnage and destruction are the domains of Ananshea. Their appetite for cruelty and violence can't be met by the simplicity of battle, and so they must torment their foes before they can be even somewhat satisfied with victory. The Skin that Walks on Teeth is as impulsive and untamed as the animals they reign over, but takes their time once the initial skirmish is over to inflict the most pain possible upon a captured opponent. Screams of pain are akin to music to Ananshea; they despise long stretches of time without their favorite melody, so they are constantly on the hunt for prey.

**Title** The Skin That Walks on Teeth

**Areas of Concern** Brutality, torture, wild animals

**Edicts** Annihilate any who would tame you, draw first blood, enjoy every kill to the fullest

**Anathema** Choose peaceful solutions over violence, hold back in a fight, tame a violent wild animal

**Religious Symbol** row of sharp teeth dripping with blood

**Sacred Animal** crocodile

**Sacred Colors** ivory, red

**Source:** `= this.source` (`= this.source-type`)
