---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Developed and widely used by students at the Kitharodian Academy in Oppara, the theatrical mutagen stimulates the creative centers of your brain. This causes your movements to become exaggerated and your voice to become clear. However, the erratic surges of inspiration overload your senses, making it difficult to focus on mundane tasks. This lasts for 1 minute.

**Benefit** You gain a +1 item bonus to Acrobatics checks, Crafting checks, and Performance checks. If you're untrained in any of these skills, your proficiency bonus is equal to your level instead of +0. You also gain a +5 feet status bonus to your Speed.

**Drawback** You take a –1 penalty to Perception checks and Will saves. After any round where you don't spend at least 1 action to Interact with an object, [[Perform]], Step, or Stride, you're [[Off Guard]] until the start of your next turn.

> [!danger] Effect: Theatrical Mutagen (Lesser)

**Source:** `= this.source` (`= this.source-type`)
