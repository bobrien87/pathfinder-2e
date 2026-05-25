---
type: deity
source-type: "Remaster"
domains: "Duty, Knowledge, Might, Zeal"
favored-weapon: "Lance"
divine-font: "Harm, Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Anticipate Peril]], Rank 4: [[Telepathy]], Rank 6: [[Collective Transposition]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Across Golarion, major wars have changed the course of history. Some have altered the political make-up of a region, with nations rising and falling. Others have left physical scars on the landscape that force citizens to relocate or change their ways of life. From stealthy scouts pointing the way to generals making plans, most soldiers understand that military strength comes from unity and communication. Followers of the Readied Strike hold that knowledge as personal faith, sometimes hard-won by those who have fallen in past battles. These covenant followers study historical battles, develop new strategies, and share them with their allies to better stand against their foes. They are also constantly honing their martial skills, with a few under the direct tutelage of intelligent magic weapons inhabited by the ghosts of deceased warriors.

**Covenant Members** intelligent weapons, sites of significant battles, spirits of soldiers

**Areas of Concern** battlefield tactics, communication, strategic planning, training regimens

**Edicts** encourage unity against common foes, maintain clear lines of communication during warfare, share training and tactics with allies

**Anathema** abandon or lie to allies, initiate violence against unidentified persons, refuse to train those seeking to learn

**Religious Symbol** lance and shield

**Source:** `= this.source` (`= this.source-type`)
