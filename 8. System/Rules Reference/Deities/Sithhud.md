---
type: deity
source-type: "Remaster"
domains: "Ambition, Cold, Undeath, Water"
favored-weapon: "Longsword"
divine-font: "Harm"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Chilling Spray]], Rank 3: [[Slow]], Rank 5: [[Howling Blizzard]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Long ago, Sithhud, the demon lord of harsh snowstorms and the frozen dead, was ousted from his realm of Jhuvumirak in the Outer Rifts by another demon lord of cold. He was not destroyed, however, and was merely reduced to a nascent demon lord as he took refuge in the labyrinthine valleys between the peaks of his former mountain domain. The deposed Frozen Lord didn't spend the intervening centuries idle. After slowly amassing an army of frozen undead, Sithhud recently led an assault to take back Jhuvumirak and in doing so, reclaimed his status as demon lord, slaying his former usurper and striking his name from all existence and memory. In addition, this foray allowed him to appropriate the concept of revenge from his enemy's portfolio. His vengeance complete, Sithhud turns his attention once again to mortalkind, hoping to regain followers among necromancers and intelligent undead who live in places regularly blanketed by snow and sleet. The Frozen Lord appears as an icy humanoid skeleton with three spidery legs. He exhorts his devotees to strike back against those who wronged them, even if it takes dozens of years.

**Title** Frozen Lord

**Areas of Concern** Blizzards, the frozen dead, revenge

**Edicts** Be as inexorable as a glacier, endure the elements, seek vengeance no matter how long it takes

**Anathema** Forgive even the smallest slights, offer shelter during a blizzard or ice storm

**Religious Symbol** icy three-fingered hand of bone

**Sacred Animal** albino wolf

**Sacred Colors** blue, white

**Source:** `= this.source` (`= this.source-type`)
