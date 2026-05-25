---
type: deity
source-type: "Remaster"
domains: "Delirium, Nightmares, Void, Star"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Grim Tendrils]], Rank 4: [[Nightmare]], Rank 5: [[Strange Geometry]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Slumbering in drowned R'lyeh, the Dreamer in the Deep is a towering monstrosity whose many tentacles reach out beyond the physical, influencing the minds of sapient beings across the Universe through their dreams. Artists and visionaries, whose creativity makes them especially susceptible to Cthulhu's influence, may wake to find themselves unconsciously inspired by memories they cannot fully grasp. As a result, countless works of art and philosophy have been produced by mortals that touch upon aspects of this Great Old One, each subtly lengthening the god's reach.

**Title** The Dreamer in the Deep

**Areas of Concern** Cataclysms, dreams, the stars

**Edicts** Create art inspired by dreams, destroy magical seals that contain destructive forces, influence the dreams of other

**Anathema** None

**Religious Symbol** complex rune surrounding an open eye

**Sacred Animal** none

**Sacred Colors** black, blue

**Source:** `= this.source` (`= this.source-type`)
