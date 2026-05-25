---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Invested]]", "[[Primal]]", "[[Tattoo]]"]
price: "{'gp': 15000}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These curving, delicate designs resemble leaves, vines, or creepers, most often wrapped around a limb, ear, or throat, or curled around specific muscles. They help you blend in among plants. You gain a +3 item bonus to Stealth checks, which increases to +4 in forests.

**Activate** R (concentrate)

**Frequency** once per day

**Trigger** A creature would detect you by Seeking

**Requirements** You're in a forest or similar natural area

**Effect** The tattoo casts [[One with Plants]] to turn you into a plant before you can be noticed. The duration of this spell is up to 8 hours.

If you've already Activated the tattoo, you can supply a separate casting of one with plants to recharge the tattoo instead of having the spell's normal effect. This allows you to Activate the tattoo again in the same day. You can do so multiple times each day, but only as many times as you continue to cast one with plants to recharge the tattoo after each use.

**Source:** `= this.source` (`= this.source-type`)
