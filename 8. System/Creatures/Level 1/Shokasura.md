---
type: creature
group: ["Asura", "Spirit"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Shokasura"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Asura"
trait_02: "Spirit"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Common, Diabolic (telepathy (touch))"
skills:
  - name: Skills
    desc: "Acrobatics +7, Deception +9, Performance +7, Religion +7, Stealth +7"
abilityMods: ["+0", "+4", "+1", "+0", "+3", "+4"]
abilities_top:
  - name: "Telepathy (Touch)"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Grieving Venom"
    desc: "**Saving Throw** DC 17 [[Will]] save <br>  <br> **Maximum Duration** 4 rounds <br>  <br> **Stage 1** 1d4 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 1d4 poison damage, and [[Enfeebled]] 2 (1 round) <br>  <br> **Stage 3** 1d4 poison damage, [[Slowed]] 1, and the creature cannot use reactions (1 round)"
armorclass:
  - name: AC
    desc: "16; **Fort** +4, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "22; **Immunities** curse; **Weaknesses** holy 2"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +9 (`pf2:1`) (agile, finesse, unholy), **Damage** 1d8 slashing plus 1 spirit"
  - name: "Melee strike"
    desc: "Thorn +9 (`pf2:1`) (agile, unholy), **Damage** 1d8 piercing plus 1 spirit plus [[Grieving Venom]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17, attack +9<br>**3rd** [[Veil of Privacy (Self Only)]]<br>**2nd** [[Stupefy]]<br>**1st** [[Charm]], [[Read Aura]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The shokasura takes on the appearance of a Small humanoid. This doesn't change the shokasura's Speed or their attack and damage modifers with their Strikes, but it might change the damage type their Strikes deal (typically to bludgeoning). The asura typically loses their thorn Strike unless the humanoid form has a similar unarmed attack. This alternate form has a specifc, persistent appearance, which the shokasura can change by performing a 1-hour ritual. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Shokasuras are tragic, wretched beings, broken by their despair at the cruel truths of reality. Many were not originally asuras but instead began as other spiritual beings who realized all of their efforts only served to propagate an unjust and unsalvageable existence. Not yet willing to admit how deep the rot lies and not yet willing to commit themselves to unmaking all they once held dear, shokasuras instead constantly test mortals and force them to prove themselves, desperately trying to assuage themselves that there are people and things still worth saving within their present circumstances. These attempts inevitably lead to disaster, as mortals either fail the shokasura's impossible expectations, or the shokasura tests their chosen mortal to ruin.

```statblock
creature: "Shokasura"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
