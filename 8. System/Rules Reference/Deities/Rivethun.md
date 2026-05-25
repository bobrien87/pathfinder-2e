---
type: deity
source-type: "Remaster"
domains: "Change, Earth, Nature, Vigil"
favored-weapon: "Mace"
divine-font: "Harm, Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Pummeling Rubble]], Rank 2: [[Summon Elemental]], Rank 7: [[Retrocognition]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

While nowhere near as large as the following of the dwarven pantheon, the worship of spirits and ancestors is still strong among the Five Kings Mountains and other dwarven population centers. Various groups and orders have existed throughout the duration of dwarven history, but none has endured as long as the Rivethun. Deriving their name from an exceptionally ancient dwarven dialect, Rivethun roughly translates to "releasers of secrets," a name that speaks to the organization's ancient traditions of animism. The members of the Rivethun, which include non-dwarves, seek to make contact with various spirits. These range from the souls of the dead and undead to elementals and fey, and to other spirits that exist beyond the typical classifications. Rivethun members communicate with these spirits, negotiating for knowledge, guidance, and favors. Serving as intermediaries, a Rivethun priest or shaman acts as a living link between dwarven civilization and the supernatural forces of reality.

**Covenant Members** spirits

**Areas of Concern** spirits, guidance, balance

**Edicts** maintain balance and understanding between the mortal and spirit world, internally cultivate yourself, serve your community

**Anathema** continually place mortal matters above spiritual ones, mislead a petitioner and fail to set it right, willingly misrepresent the will of spiritual entities

**Religious Symbol** gem floating above a diamond of metal

**Source:** `= this.source` (`= this.source-type`)
