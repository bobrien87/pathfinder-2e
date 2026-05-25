---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Disarm]]", "[[Finesse]]", "[[Nonlethal]]", "[[Reach]]", "[[Trip]]"]
price: "{'gp': 500}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking whip* is crafted from the vine of a dangerous plant creature. It deals bludgeoning or slashing damage, according to the vine attack of the creature it was harvested from. For example, collecting a vine from an assassin vine would result bludgeoning damage, while one from a mandragora or viper vine would deal piercing damage.

**Activate** `pf2:3` (concentrate, manipulate)

**Requirements** You have soil or sand within your reach

**Effect** You Release the weapon and plant it in the ground, where it takes root and fights on its own against the last enemy you attacked or the nearest enemy to it if your target has been defeated.

The weapon has a space of 5 feet, acts on your initiative, and gains two actions. It doesn't block or impede enemies attempting to move through that space, nor does it benefit from or provide flanking. The weapon can't use reactions, and it acts on your turn.

While Activated, a vine whip makes Strikes with an attack modifier of +22 plus its item bonus to attack rolls (normally +24 total). It uses the weapon's normal damage but has a +0 Strength modifier. The whip's abilities that automatically trigger on a hit or critical hit still function, but the weapon can't be Activated or benefit from any of your abilities while rooted.

Each round, when the vine whip is finished using its actions, attempt a DC 6 flat check. On a failure, the Activation ends and the vine whip becomes inanimate. You can't Activate the item again for 10 minutes. Removing the vine whip from the ground takes an Interact action.

While rooted, the vine whip gains fast healing 1.

**Craft Requirements** The initial raw materials must include the vine from a plant creature with a vine attack.

**Source:** `= this.source` (`= this.source-type`)
