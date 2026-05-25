---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Apex]]", "[[Deadly d8]]", "[[Disarm]]", "[[Finesse]]", "[[Invested]]"]
price: "{'gp': 70000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Crafted from flawless jade, the guard of this rapier takes the form of a twisting serpent with the blade thrusting from its open mouth. This rapier functions as a +3 greater striking quickstrike rapier. While wielding the rapier, your movement doesn't trigger reactions when you Stride, [[Balance]], or [[Tumble Through]]. When you invest the rapier, you either increase your Dexterity modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate** R (concentrate)

**Frequency** once per day

**Trigger** You fail, but don't critically fail, an attack using the viper rapier

**Effect** The tip of the rapier briefly takes the form of a viper's head, and the blade twists and contorts, biting the target you missed. The target is affected as if successfully poisoned with cave worm venom (DC 43).

**Activate** R (concentrate)

**Trigger** A creature misses or critically misses you with an attack

**Effect** With a slight, obviously mocking bow or curtsy, you Step.

**Activate** `pf2:2` (manipulate)

**Frequency** once per hour

**Effect** You twirl your rapier in a serpentine pattern, causing your form to become a blur of motion. You're [[Concealed]] for 1 minute or until you take a hostile action. While you're concealed, you also gain a +2 circumstance bonus to Reflex saving throws.

> [!danger] Effect: Viper Rapier

**Source:** `= this.source` (`= this.source-type`)
