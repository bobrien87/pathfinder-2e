---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 155}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This vial of murky, acrid-smelling liquid is derived from a blend of strange blood, typically coming from aberrations and cryptids. It has no special properties when used alone, but if you drink one shortly before drinking an alchemical elixir, you enhance the elixir's duration. Many tales of mysterious cryptids are actually based on encounters with people suffering the aftereffects of such concoctions.

After drinking a baleblood draft, the next elixir you drink within 1 minute that has a duration of at least 1 minute and at most 1 hour has its duration extended by 50% (so a lesser cheetah's elixir lasts for a minute and a half instead of 1 minute).

However, after pairing baleblood draft with another elixir, you suffer an eerie side effect for 1 week. This side effect never causes serious harm, although it might be inconvenient and is always ominous in appearance. All elixirs made in the same batch cause the same side effect. Drinking another draft with the same side effect extends the side effect's duration by another week, and drinking one with a different side effect causes you to suffer both effects simultaneously.

**Source:** `= this.source` (`= this.source-type`)
