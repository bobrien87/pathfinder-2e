---
type: deity
source-type: "Remaster"
domains: "Indulgence, Might, Secrecy, Zeal"
favored-weapon: "Glaive"
divine-font: "Harm"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Summon Animal]], Rank 2: [[Enlarge]], Rank 8: [[Quandary]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Baphomet, Lord of the Labyrinth, is the demon lord of beasts, dungeons, and traitors. Baphomet was originally a consort of Lamashtu who achieved demon lord status after escaping from imprisonment in a labyrinth constructed by Asmodeus. Baphomet appears as an enormous emaciated minotaur with feathered wings and a goat-like head that bears three horns, as well as a blazing pentagram branded into his forehead. As a lord of beasts, he grants his blessings to wild animals (like bears, dinosaurs, and sharks) who kill humanoids, whether accidentally or intentionally. Baphomet's cults are among the most prolific in Golarion—humandominated secret societies devoted to the demon lord are present in many cities and may have members ensconced in positions of political power.

**Title** Lord of the Labyrinth

**Areas of Concern** Beasts, dungeons, traitors

**Edicts** Confuse paths and roads, outwit your foes instead of overpowering them, unleash beasts to kill others

**Anathema** Kill something that cannot significantly harm you, bargain with Asmodeus

**Religious Symbol** brass bull head

**Sacred Animal** auroch

**Sacred Colors** gold, red

**Source:** `= this.source` (`= this.source-type`)
