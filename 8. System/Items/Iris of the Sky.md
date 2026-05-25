---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Concussive]]", "[[Fatal aim d12]]"]
price: "{'gp': 240}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking jezail* is built from white hot metal and has a ruby fused into the palm wood stock. When the *iris of the sky* misfires, you take 5 persistent,fire damage.

The first firearm of this type came as the result of a gunslinger who entreated an ifrit, wishing for the might of the desert sun. The weapon constantly glows and burns with a brilliant intensity. The firearm has since belonged to an extensive string of users and been replicated several times, though each wielder of the weapon, whether the original or one of its copies, has eventually ended up as a charred husk, slain by fire in battle or unusual accidents that no one could quite explain except, perhaps, the ifrit.

**Activate—Sear the Sky** `pf2:1` (concentrate)

**Frequency** once per minute

**Effect** You focus the solar energy housed in the ruby to release a gout of solar flame instead of a bullet. Make a Strike with the iris of the sky. All damage from this Strike is fire damage and the target takes an additional 1d6 fire damage and 1d6 persistent,fire damage.

**Activate—A Wish Granted With Inevitable Fire** `pf2:2` (concentrate, manipulate, fortune)

**Frequency** once per minute

**Effect** You make a wish into the iris of the sky, yearning for it to strike true, and then fire. Strike against a foe with the iris, rolling the attack roll twice and taking the better result. If the attack is a failure, you take 5 persistent fire damage.

**Source:** `= this.source` (`= this.source-type`)
