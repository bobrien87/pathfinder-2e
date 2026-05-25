---
type: deity
source-type: "Remaster"
domains: "Death, Nature, Nightmares, Secrecy"
favored-weapon: "Jaws, Dagger"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Vanishing Tracks]], Rank 3: [[Paralyze]], Rank 4: [[Vision Of Death]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The guardian of deadly secrets and dangerous places, Kalekot is a bogeyman to most, murderer of the guilty and devourer of those who trespass. To those that society can't punish, Kalekot is executioner, striking from the shadows and leaving bodies to rot on the ground. To those lost at night, Kalekot is a silent follower, a guardian from danger. Those few who have glimpsed him describe a figure with withered skin and a snake's twisting spine. He always conceals his features behind an eyeless mask, its mouth filled with serpent's teeth, each fang the size of an elephant's tusk.

**Title** The Winnower

**Areas of Concern** Fear, silence, safekeeping, the reviled

**Edicts** Spread fear in others, hide dangerous secrets, shock the self-righteous, kill the guilty to protect the innocent

**Anathema** Abuse someone you have accepted power over, allow a victim to escape due to gloating, snivel before authority, shout

**Religious Symbol** Snake piercing its head with a dagger

**Sacred Animal** Two-headed animals

**Sacred Colors** gray, red

**Source:** `= this.source` (`= this.source-type`)
