---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]"]
price: "{'gp': 24000}"
usage: "other"
bulk: "20"
source: "Pathfinder #214: The Broken Palace"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An *essence forge* consists of a large stone workbench with a receptacle for fuel built into the left side. Sparkling crystals are embedded across the forge's structure, with additional flourishes made from a different material, as appropriate to the type of forge.

*Life forges* are adorned with fossilized bones and petrified wood. They're used to craft items associated with the divine and primal magic traditions. One must attempt a Nature or Religion check to prime a *life forge*.

*Matter forges* are decorated with strips of precious metal. They can be used to craft items associated with the arcane and primal magic traditions. One must attempt an Arcana or Nature check to prime a *matter forge*.

*Mind forges* are accentuated with glittering gemstones. They can be used to craft items associated with the arcane and occult magic traditions. One must attempt an Arcana or Occultism check to prime a *mind forge*.

*Spirit forges* are emblazoned with strange runes and obscure symbols enhanced by different pigments. They can be used to craft items associated with the divine and occult magic traditions. One must attempt an Occultism or Religion check to prime a *spirit forge*.

**Activate—Prime the Forge** 1 minute (concentrate, manipulate)

**Requirements** The *essence forge* doesn't currently contain any stored essence

**Effect** You prepare the *essence forge* for use by placing raw materials in its receptacle then spend an hour concentrating on the forge, using your own magical potential to consume the materials. The combined gp value of the raw materials sets the maximum price of the item you can craft with the *essence forge*. An *essence forge*'s receptacle can hold no more than 3 Bulk of raw materials, so coins, gemstones, or small valuable objects or items make for the best sources of fuel. Attempt an DC 40 [[Arcana]] check, DC 40 [[Nature]] check, DC 40 [[Occultism]] check, or DC 40 [[Religion]] check as appropriate for the tradition of *essence forge* you're using to focus your magical potential on the receptacle.
- **Critical Success** The raw materials are consumed, and the *essence forge* stores essence equal to the value of the raw materials. Additional essence overflows back into you, granting a +3 item bonus to the skill you used to Prime the Forge for the next 24 hours.
- **Success** The raw materials are consumed, and the *essence forge* stores essence equal to the value of the raw materials.
- **Failure** The raw materials are consumed, but the burn is inefficient, and the *essence forge* stores essence equal to half the value of the raw materials.
- **Critical Failure** The raw materials are consumed and lost, but no essence is stored in the forge; the raw materials are wasted.

**Activate—Craft an Item** 2 hours (concentrate, manipulate)

**Requirements** The *essence forge* has been primed with raw materials equaling or exceeding the value of the item you intend to craft, and you are not [[Fatigued]]

**Effect** You place your hands atop the forge's workspace and focus your concentration on the essence contained within the forge. Choose an item whose formula you have and whose level is equal to or less than the *essence forge*'s level, or choose an [[Essence Charm]]. The *essence forge* begins to construct that item as you concentrate, causing an increasingly realistic illusion of the item to come into focus atop the forge's workspace. Attempt a Crafting check with a DC determined by the forge's type (lesser, moderate, or greater); this check earns Forge Points (using the Victory Point system). You can sustain this activation for up to 8 hours; each time you sustain the activation, attempt another Crafting check to earn Forge Points. When you choose to end the activation, you become fatigued, and any remaining essence stored in the forge dissipates with no further effect. Consult the *Essence Forge* Crafting section below to determine if you were successful in crafting the item you chose.

**Activate—Absorb Essence** `pf2:1` (concentrate, healing, manipulate)

**Requirements** The *essence forge* contains essence

**Effect** You absorb the essence in the forge, emptying it and allowing it to be primed. If the essence value in the forge is equal to or greater than 5,000 gp, the forge heals you for @Damage[(8d8+30)[healing]] HP. Otherwise the absorbed essence has no effect.

*Essence Forge* CraftingWhen you finish crafting with an *essence forge*, consult the following to determine how successful you were.

**0 or fewer Forge Points:** The essence was tainted or your concentration was lacking. An illusory object manifests, but it's a non-magical, worthless level 0 replica of the item you intended to craft.

**1–3 Forge Points:** The item you craft is functional but temporary. It falls apart after it's activated or after 24 hours, whichever comes first.

**4–5 Forge Points:** You successfully craft the item.

**6 or more Forge Points:** You successfully craft the item, and it works better than expected. Choose one of the following enhancements to add to the item:

- If the item has an activation that has a frequency of once per day, that activation can be made an additional time each day.
- If the item has an activation that has a save DC or Strike modifier, that DC or Strike gains a +1 bonus.
- If the item is an invested item, it grants a +1 item bonus to initiative checks as long as you have it invested.
- The item is well crafted and can be sold for 60%

**Source:** `= this.source` (`= this.source-type`)
