---
type: deity
source-type: "Remaster"
domains: "Ambition, Fire, Lightning, Zeal"
favored-weapon: "Longspear"
divine-font: "Harm, Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Ill Omen]], Rank 2: [[Floating Flame]], Rank 7: [[Fiery Body]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Fires and explosions of all kinds are Lubaiko's passion, from an ember that ignites a flour mill to an outrage that rips through a nation. She is the powder keg whose fuse has burned down, erupting into something momentous, be it for better or for worse. Roaming throughout the sky above Golarion, she delights in throwing her bolts into the fields and the minds of people, whenever conditions permit and wherever they may fall. Some believe the smoke from Lubaiko's fires are curses and misfortune flying up into the air to spread throughout the land. Yet Lubaiko's blazes also often clear the way for new growth.

**Title** The Spark in the Dust

**Areas of Concern** Wildfire, bad luck, inspiration, turmoil

**Edicts** Set fires, change the world, act with ambition or not at all

**Anathema** Calm a crowd, douse a fire, sleep in the same place three nights in a row

**Religious Symbol** exploding sphere

**Sacred Animal** locust

**Sacred Colors** black, red

**Source:** `= this.source` (`= this.source-type`)
