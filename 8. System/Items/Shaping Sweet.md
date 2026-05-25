---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 6}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Many inhabitants of the First World can shape their environment around them; weaker creatures can only make minor changes, while powerful entities such as the Eldest can remake entire landscapes. A *shaping sweet* is a gelatinous, fruit-flavored candy that confers a whisper of this ability on you when you eat it. For 1 hour after eating a *shaping sweet*, you can make each of the following changes to your surroundings with an Interact action. You can make each change only once.

- **Alter Weather** You create or eliminate minor precipitation in a @Template[type:emanation|distance:30].
- **Fairy Ring** A ring of flowers and mushrooms appears in a @Template[type:burst|distance:10] around you, restoring 1 Hit Point at the start of each of your turns to a randomly chosen fey creature within. The ring lasts for 1 minute.
- **Foliate Vegetation** grows around you in a 10-foot radius burst, creating light undergrowth that lasts for 1 minute.
- **Terrain Shift** The ground in your space rises or falls by 5 feet, remaining at that height for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
