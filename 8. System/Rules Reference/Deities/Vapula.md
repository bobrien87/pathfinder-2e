---
type: deity
source-type: "Remaster"
domains: "Knowledge, Protection, Secrecy, Wealth"
favored-weapon: "Staff"
divine-font: "Harm"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Illusory Object]], Rank 3: [[Bottomless Stomach]], Rank 4: [[Liminal Doorway]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

With a greed that rivals that of the oldest dragons, Vapula relishes knowledge. He particularly savors the moment when one learns something new and has to recontextualize everything as their reality changes. In the chase for revelation, he has acquired quite the collection and developed a knack for cataloging and security. All that is lost is found in his vaults. The prayers of the widower who lost his ring, the pup whose human forgot them, the knight whose sword was knocked into the crevasse in their most dire hour—their quiet offers cross the Keeper of the Pyrite Vault's ears before any others. For easy favors, wishes can come true. Devils, demons, archmagi, and scores of angels come to account with Vapula, each knowing any treasures or threats they deposit are safe and accounted for. Threats from Asmodeus himself could not ply Vapula, for the Exchequer's word is his bond, and he is all the more respected for it. Those that meet with Vapula encounter a living stone statue of a horned man wearing an elegant robe, his visage changing every time one looks away.

**Title** The Exchequer

**Areas of Concern** Discovery, hubris, scholars

**Edicts** Finders keepers, speak with others in their native language, ask more questions than you give answers

**Anathema** Work in approximations, renegotiate, fail to uphold your word

**Religious Symbol** rearing griffon

**Sacred Animal** lion

**Sacred Colors** white, yellow

**Source:** `= this.source` (`= this.source-type`)
