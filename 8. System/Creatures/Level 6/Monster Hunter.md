---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Monster Hunter"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +15, Stealth +13, Survival +11, Monster Lore +13"
abilityMods: ["+4", "+3", "+3", "+1", "+1", "+1"]
abilities_top:
  - name: "Favored Game"
    desc: "A monster hunter specializes in bringing down certain non-humanoid creatures. These favored game are typically animals and beasts, but an individual might hunt dragons, plants, or more specialized creatures like tigers or manticores."
  - name: "Primal Fear"
    desc: "When the monster hunter hits a creature that qualifies as their favored game, that creature is [[Frightened]] 1 (or [[Frightened]] 2 on a critical hit)."
armorclass:
  - name: AC
    desc: "22; **Fort** +15, **Ref** +11, **Will** +13"
health:
  - name: HP
    desc: "105"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within your reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> You lash out at a foe that leaves an opening. Make a melee Strike against the triggering creature. If your attack is a critical hit and the trigger was a manipulate action, you disrupt that action. This Strike doesn't count toward your multiple attack penalty, and your multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greataxe +15 (`pf2:1`) (magical, sweep), **Damage** 1d12+8 slashing plus [[Primal Fear]]"
  - name: "Ranged strike"
    desc: "Composite Longbow +14 (`pf2:1`) (deadly d10, propulsive, reload 0, volley 30, range 100 ft.), **Damage** 1d8+6 piercing plus [[Primal Fear]]"
spellcasting: []
abilities_bot:
  - name: "Hunter's Onslaught"
    desc: "`pf2:1` **Frequency** once per hour <br>  <br> **Requirements** The monster hunter isn't [[Fatigued]] <br>  <br> **Effect** The monster hunter leads an attack against their monstrous foe. The monster hunter chooses an enemy they can see that qualifies as their favored game. The monster hunter becomes [[Fascinated]] by that creature and gains 10 temporary Hit Points that last as long as the onslaught does. During the onslaught, the hunter gains a +8 status bonus to damage rolls against the designated enemy, and allies in a 30-foot aura around the hunter gain half that bonus. The onslaught lasts for 1 minute or until either the monster hunter or the designated creature falls [[Unconscious]]."
  - name: "Sudden Charge"
    desc: "`pf2:2` The monster hunter Strides twice and makes a melee Strike."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Some mercenaries eschew the complications of politics and fealty and just get paid to hunt monsters. It's a straightforward form of mercenary service, often dangerous in the extreme, but one that can yield glory and fame.

Whether they're hired to wage war, protect a caravan, or infiltrate an impenetrable fortress, there's ample work for mercenaries all over Golarion.

```statblock
creature: "Monster Hunter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
