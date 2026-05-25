---
type: deity
source-type: "Remaster"
domains: "Decay, Destruction, Nightmares, Void"
favored-weapon: "Warhammer"
divine-font: "Harm"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Ill Omen]], Rank 5: [[Synaptic Pulse]], Rank 9: [[Unfathomable Song]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Azathoth is the Daemon Sultan and the Primal Chaos, a roiling mass of destructive and transformative power the size of a sun, dwelling in the darkness between the stars deep in the center of the universe. There, masked from mortal sight by a veil of swirling colors, he is surrounded by the other Outer Gods that make up his court, dancing and cavorting about him endlessly, filling the void with the sound of ghastly flutes. Azathoth is utterly unaware of and uncaring toward those few who have come to revere and worship him. It is precisely this blind, uncaring nature that makes Azathoth the perfect embodiment of a blind, uncaring universe. Azathoth's name, however, has great power over the Outer Gods when properly invoked. He has also sometimes been summoned by mortal priests—and though these summons attract only a tiny sliver of his attention and manifest as a form other than that of the Primal Chaos, they nevertheless lead to destruction on a massive scale.

**Title** The Primal Chaos

**Areas of Concern** Entropy, madness, mindless destruction

**Edicts** Gather a court of devotees, create discordant piping or babbling

**Anathema** None

**Religious Symbol** eight pointed star

**Sacred Animal** none

**Sacred Colors** black, white

**Source:** `= this.source` (`= this.source-type`)
