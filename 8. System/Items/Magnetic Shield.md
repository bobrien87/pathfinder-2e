---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Aura]]"]
price: "{'gp': 130}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Copper rings spiral around this [[Steel Shield]]. Twin electrical probes near the grip can socket into a jar of moderate (or higher leveled) Bottled Lightning, which takes 3 Interact actions to install.

**Activate** `pf2:1` (manipulate)

**Requirements** A *bottled lightning* is installed in the shield

**Effect** The shield becomes an electromagnet for 3 rounds. When an activated magnetic shield is raised, the circumstance bonus increases by 1 against attacks made with weapons primarily made of metal. If you use a [[Shield Block]] against a creature attacking you with such a weapon, you also gain a +1 item bonus to [[Disarm]] attempts against that weapon until the end of your next turn. The activation uses up the *bottled lightning*, and the shield can't be activated again until a new one is installed.

**Source:** `= this.source` (`= this.source-type`)
