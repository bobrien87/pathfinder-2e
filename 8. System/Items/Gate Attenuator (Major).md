---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "worn"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When you invest the *major gate attenuator*, you either increase your Constitution modifier by 1 or increase it to +4, whichever would give you a higher score.

*Gate attenuators* are typically worn near the body's core and are shaped like portals or passageways, making literal the elemental gates kineticists possess within their bodies. The appearance can vary from a simple disk with a hole in the middle to a design matching a city gate of a particular settlement. If you're a kineticist, the attenuator grants you a +2 item bonus to your impulse attack modifier (but not to your impulse DC). When you invest a *gate attenuator*, attune it to one element of your choice. Designs on the attenuator's surface transform to match that element, and the attenuator gains the element's trait until it's no longer invested or is attuned to a different element.

**Activate - Elemental Spell** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** The *gate attenuator* casts an 8th-rank spell, with a spell attack modifier of +27 and a spell DC of 37.If you're a kineticist and the spell's element matches one of your kinetic elements, you can use your impulse attack modifier instead of the spell attack modifier or your impulse DC instead of the spell DC. The spell corresponds to the element the item is attuned to, and it gains that element's trait if it doesn't already have it:

**air** [[Whirlwind]]

**earth** [[Earthquake]]

**fire** [[Boil Blood]]

**metal** [[Rust Cloud]]

**water** [[Whirlpool]]

**wood** [[Pollen Pods]]

**Source:** `= this.source` (`= this.source-type`)
