---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Auditory]]", "[[Consumable]]", "[[Emotion]]", "[[Incapacitation]]", "[[Magical]]", "[[Mental]]", "[[Missive]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate, manipulate)

A captivating score is a piece of parchment prepared for musical notation, long enough for a short song. You must be trained in Performance to properly compose this missive (or trained in an appropriate Lore skill your GM allows). You choose one of the emotions described below and write a musical composition to convey that emotion about a subject of your choice, typically a person or group. When activated, the missive plays a note-perfect rendition of the inscribed score. Each creature that can hear the score must succeed at a DC 28 [[Will]] save or be influenced to feel the emotion you chose toward the subject of your composition. This lasts for 1 hour, typically returning the creature to its initial attitude unless new events have altered their attitude long-term.

- **Positive** Your song engenders sympathy, adoration, joy, or a similar emotion. An affected creature's attitude toward the subject improves by one step, such as from indifferent to friendly.
- **Negative** Your song spurs anger, sadness, jealousy, or a similar emotion. An affected creature's attitude toward the subject worsens by one step, such as from indifferent to unfriendly.

When composing this missive, you can add a small notation or illustration of a type of instrument. If you do, the music sounds like that instrument, and if you didn't specify, it sounds vaguely like a recorder. The choice of a louder instrument doesn't make the music carry farther.

**Source:** `= this.source` (`= this.source-type`)
