---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Deadly d10]]", "[[Magical]]", "[[Volley 30]]"]
price: "{'gp': 360}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking [[Hauling]] longbow* is lined with the flesh of a fallen hydra and ornate carvings on the grip that depict the hydra's number of heads it had before it was slain. When you wield the bow in combat, you regain 2 Hit Points at the start of each of your turns.

**Activate—Two-Headed Arrow** `pf2:2` (manipulate)

**Effect** You imbue your arrow with the properties of a hydra, splitting it in two and sending each at a different foe. Make two ranged Strikes, each against a separate target. Both targets must be in your line of sight, and within 50 feet of you. Both Strikes count toward your multiple attack penalty, but the penalty doesn't increase until after you've made both attacks. Additionally, after using this ability, you do not regain Hit Points from wielding the bow on your next turn.

**Activate—Five-Headed Arrow** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You make a powerful Strike propelled by the ferocity of a hydra at a target within your first range increment. If your Strike is successful, the arrow deals damage as normal and then passes through the target, splitting into four pieces. Choose four other targets within 30 feet of the original target and make a single ranged Strike with your multiple attack penalty, comparing the result to each secondary target's AC. After using this ability, you do not regain Hit Points from wielding the bow until after your next daily preparations.

**Craft Requirements** The initial raw materials must include the flesh from a severed head of a hydra.

**Source:** `= this.source` (`= this.source-type`)
