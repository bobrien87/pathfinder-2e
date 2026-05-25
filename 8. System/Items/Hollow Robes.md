---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Comfort]]", "[[Illusion]]", "[[Invested]]", "[[Mythic]]"]
price: "{'gp': 3000}"
bulk: "1"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These heavy cloth garments function as a set of *+2 resilient explorer's clothing*. They feature multiple stylish layers, voluminous sleeves, and long strings of Thassilonian runes along the hems. The robes employ potent illusion magic, sufficient to convince the wearer and any attackers that a devastating blow is nothing more than a flesh wound.

**Activate—Empty Robes** `pf2:1` (concentration)

**Frequency** once per hour

**Effect** The wearer becomes [[Invisible]] inside the robes for one minute. Since the wearer's gear (including the robes) remain visible, they don't become [[Concealed]], but they can't be visually identified unless the viewer can see invisible creatures. The unsettling nature of this effect grants the wearer a +2 item bonus to Intimidation checks made while the robes appear to be empty.

**Activate—Hollow Target** `pf2:r` (concentration)

**Requirements** Empty Robes is in effect

**Trigger** You take persistent damage or a critical hit from a Strike

**Effect** Spend 1 Mythic Point. You momentarily transform yourself into an illusory duplicate, rendering yourself "hollow" to the triggering damage or Strike. The damage from a critical hit Strike is reduced to 0. All persistent damage you're currently taking ends.

**Activate—Unseen Magic** `pf2:1` (spellshape)

**Requirements** Empty Robes is in effect

**Effect** If your next action is to Cast a Spell that doesn't have the manipulate trait, that spell gains the subtle trait.

**Craft Requirements** You must be a mythic arcane spellcaster capable of casting invisibility.

**Source:** `= this.source` (`= this.source-type`)
