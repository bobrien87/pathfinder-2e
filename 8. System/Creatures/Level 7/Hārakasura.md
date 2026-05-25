---
type: creature
group: ["Asura", "Spirit"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hārakasura"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Asura"
trait_02: "Spirit"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: "Common, Diabolic (telepathy 30 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +15, Athletics +19, Intimidation +15, Performance +15, Stealth +15"
abilityMods: ["+6", "+4", "+4", "+2", "+2", "+4"]
abilities_top:
  - name: "Telepathy (30 feet)"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "25 all-around vision; **Fort** +15, **Ref** +17, **Will** +13"
health:
  - name: HP
    desc: "130; **Immunities** curse"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "Dual Mind"
    desc: "`pf2:r` **Trigger** The hārakasura fails a saving throw against a mental efect <br>  <br> **Effect** The hārakasura shunts the efect into one of their minds, rendering them temporarily insensible. They change their result to a success, but one of their bodies hangs limply until the end of their next turn. During this time, the hārakasura is [[Clumsy]] 2; takes a –10-foot circumstance penalty to their Speed; and can't use Dual Mind, Dance of Destruction, or Reactive Strike."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within your reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> You lash out at a foe that leaves an opening. Make a melee Strike against the triggering creature. If your attack is a critical hit and the trigger was a manipulate action, you disrupt that action. This Strike doesn't count toward your multiple attack penalty, and your multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Kukri +18 (`pf2:1`) (agile, trip), **Damage** 1d6+9 slashing plus 2d6 bleed plus 1d4 spirit"
  - name: "Melee strike"
    desc: "Claw +18 (`pf2:1`) (agile, unarmed), **Damage** 1d6+9 slashing plus 1d4 spirit"
spellcasting: []
abilities_bot:
  - name: "Dance of Destruction"
    desc: "`pf2:1` **Requirements** The hārakasura's last action was a Strike that dealt damage <br>  <br> **Effect** The hārakasura Strides up to 10 feet and Strikes."
  - name: "Glorious Visage"
    desc: "`pf2:1` The asura sanctifies themselves as either holy or unholy, gaining the trait corresponding to their choice and losing the opposing trait; their strikes, spells, and abilities also gain the trait corresponding to their choice. The asura also gains weakness 5 to the opposing sanctification and loses any weakness to its chosen sanctification. The choice is permanent until the asura uses this ability to change their sanctification."
  - name: "Wound Thief"
    desc: "`pf2:1` The hārakasura touches an adjacent creature that is taking persistent bleed damage. If the hārakasura has the holy trait, it ends the persistent bleed efect immediately and restores 2d6 Hit Points to the target; this is a healing and vitality effect. If the hārakasura has the unholy trait, it causes the target to immediately take damage equal to its persistent bleed value, and the hārakasura gains temporary Hit Points equal to the damage taken until the start of its next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Hārakasuras appear as two f gures that are intrinsically intertwined, moving in complete tandem. In truth, they're a single being with a split heart and split wills, switching between virtue and god-defying ruin. Hārakasuras are above all beings of kindness and charity, yet every kind deed they seek to do only emphasizes the broken nature of the world—for if all were given what they needed, charity would never be required. Hārakasuras thus dub themselves as thieves and plunderers, stealing from one corner of the world to give to another, torn between their loyalty toward helping people and their despair at a horrif c existence where people cannot survive without their help.

```statblock
creature: "Hārakasura"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
