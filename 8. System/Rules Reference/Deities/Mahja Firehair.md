---
type: deity
source-type: "Remaster"
domains: "Family, Fire, Perfection, Toil"
favored-weapon: "Scimitar"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 3: [[Blazing Dive]], Rank 5: [[Mantle Of The Magma Heart]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

As a mortal, Mahja Firehair was a follower of Sarenrae and the warlord of the Burning Sun hold, which was initially made up of outcasts from other holds. Through Mahja's heroic and fearsome reputation, she oversaw the rapid growth and expansion of her people. After her death, she defeated the reigning orc god of fire, Sezelrian, in the Crucible and became a deity. Mahja carries much of Sarenrae's teachings into her own values as a goddess and shares Sarenrae's affinity for fire, but her primary concern is teaching her followers to bring glory to all orcs and to instill a sense of willing sacrifice into her followers if that is what's required to achieve this goal.

Much like Sarenrae, Mahja values fire's literal and figurative cleansing. However, she believes redemption should be earned, rather than given freely. In fact, Mahja strongly believes in proving one's worth in all aspects of life. She routinely tested people before her ascension and was known to ask leading questions and request demonstrations of people's abilities before she took them seriously. She also commonly gave people difficult tasks before considering trades, deals, or alliances. However, she was fiercely loyal to those who proved their worth to her.

**Title** Matron of Rites

**Areas of Concern** Community, fire, trials of worth

**Edicts** Bring honor and glory to orcs, build up your community, seek personal perfection

**Anathema** Undermine your community, seek personal glory, grant redemption to the unworthy

**Religious Symbol** flaming heart

**Sacred Animal** salmon

**Sacred Colors** gold, green

**Source:** `= this.source` (`= this.source-type`)
