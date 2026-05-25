---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]"]
price: "{'gp': 30}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These discrete prosthetics have been the secret behind more than a few salacious rumors getting out among Taldan high society. This functions like a [[Magical Prosthetic Eye]], but with an added benefit.

**Activate** `pf2:1` command

**Frequency** once per day

**Effect** You whisper "spy for me" to the eye, which removes itself from your eye socket and begins to relay its signal to you even at range. Although it can't move on its own, you can place the eye in a discrete location (using your Stealth DC) to avoid detection. For 10 minutes, you can see what the eye sees as long as you're within 100 feet of the eye. The eye's signal can penetrate most barriers but is blocked by lead of any thickness, as well as denser materials. The eye's signal is visual only.

**Source:** `= this.source` (`= this.source-type`)
