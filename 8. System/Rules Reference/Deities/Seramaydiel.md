---
type: deity
source-type: "Remaster"
domains: "Air, Confidence, Creation, Passion"
favored-weapon: "Blowgun"
divine-font: "Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Seashell Of Stolen Sound]], Rank 4: [[Infectious Melody]], Rank 5: [[Hallucination]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

It is said that the song of Seramaydiel's harp can calm the soul of the broken hearted, strengthen those headed into righteous battle, and lure evildoers into uncertain death. A battle-hardened warrior in her own right, she much prefers to solve conflicts with conversation instead of confrontation, for a soul lost in battle is one less soul that can create beautiful things. However, she will not shy away from fighting for what is right, and her songs are known to bolster those charging forth on a battlefield.

**Title** Lady of Inspired Notes

**Areas of Concern** Communication, inspiration, music

**Edicts** Create music in public where strangers can hear and be inspired by you, compose original poetry about that which you are passionate about, support the arts in any way you can

**Anathema** Destroy musical instruments, disparage others who create music, encourage others to not support artisans

**Religious Symbol** gold-and-silver harp

**Sacred Animal** katydid

**Sacred Colors** gold, silver

**Source:** `= this.source` (`= this.source-type`)
