---
type: creature
group: ["Aeon", "Monitor"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Venator"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aeon"
trait_02: "Monitor"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+24; [[Darkvision]]"
languages: "Common, Diabolic, Empyrean, Utopian"
skills:
  - name: Skills
    desc: "Acrobatics +25, Arcana +23, Athletics +23, Stealth +27, Survival +24"
abilityMods: ["+6", "+8", "+4", "+4", "+5", "-2"]
abilities_top:
  - name: "Locate Target"
    desc: "A venator is assigned an individual target or small group of targets when they are created. The venator can sense the direction of their nearest target while on the same plane as it. If there are none, they can sense the plane where most of their targets can be found."
  - name: "Discharging Bolt"
    desc: "When the venator damages a creature with their crossbow, the bolt embeds in the target, dealing 2d6 persistent,electricity damage. The creature can remove the bolt and end the persistent damage with an Interact action but takes 1d6 electricity damage as part of removing the bolt."
armorclass:
  - name: AC
    desc: "33; **Fort** +21, **Ref** +25, **Will** +24"
health:
  - name: HP
    desc: "230; **Immunities** disease, fear effects, emotion; **Weaknesses** electricity 15"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Ranged strike"
    desc: "Crossbow +27 (`pf2:1`) (magical, reload 1, range 120 ft.), **Damage** 2d8+12 piercing plus 1d10 electricity"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 33, attack +0<br>**7th** [[Interplanar Teleport (to plane indicated by locate target only)]]<br>**4th** [[Translocate]]<br>**2nd** [[Invisibility]] (At Will), [[Revealing Light]] (At Will)"
abilities_bot:
  - name: "Mark Target"
    desc: "`pf2:1` The venator releases a ball of light at a target within 60 feet, lighting it up with a magical aura that's constantly visible to the venator. The target can avoid becoming marked with a successful DC 30 [[Reflex]] save. While marked, the target finds it difficult to deal with the venator and their allies. The target takes a –1 status penalty to all attacks against the venator and other aeons, as well as to saving throws against efects from the venator and other aeons. The venator can Sustain this efect to designate up to 5 other creatures as trusted allies, causing the target to take the same penalties against these allies. The venator can Dismiss the mark. Otherwise, it fades away naturally after 1 day. <br>  <br> > [!danger] Effect: Venator's Mark"
  - name: "Overloaded Arc"
    desc: "`pf2:2` The venator releases lightning from their body in a @Template[type:line|distance:120], dealing @Damage[4d10[electricity]|options:area-damage] damage (DC 33 [[Reflex]] save). The lightning also arcs, damaging any creature embedded with a venator's bolt within 120 feet even if it isn't in the line. The venator is then [[Slowed]] 1 for 1 round."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Unlike most aeons, venators spend much of their time in the mortal Universe. Axiomites build these fgures of brass and gears to hunt their enemies. Although capable combatants on their own, venators frequently act as trackers for other aeons, leading a group of vigilias to secure a criminal or guiding a bythos to its targets.

Each venator is forged with its targets already assigned, a scrap of axiomite formula integrated in the gears that whir beneath their armor. The targets are narrowly defned by the formula and are usually a single named target, a family, or a small group that directly participated in an event.

A venator's targets rarely threaten the balance of reality overtly; instead, they're often privy to certain secrets or new magical theories.

As a result, even the venator rarely knows why it has been assigned a given target. Recently forged venators are incredibly thorough in their work, methodically destroying the body of their target and any nearby objects (like notes, books, or even graffti) that might contain secrets.

Successful venators are left without targets and are abandoned to their own devices. They're generally eager to fnd a new purpose, even if it's a temporary one from a mortal summoning. Many eventually extend their original missions, choosing new targets similar to their previous ones or, in some cases, continuing to chase the souls of their original targets.

```statblock
creature: "Venator"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
